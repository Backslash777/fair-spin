const http = require('http');

const expression = process.argv.slice(2).join(' ');
if (!expression) {
  console.error('Usage: node tools/cdp-eval.cjs <JavaScript expression>');
  process.exit(2);
}

http.get('http://127.0.0.1:9222/json/list', response => {
  let body = '';
  response.on('data', chunk => { body += chunk; });
  response.on('end', () => {
    const page = JSON.parse(body).find(item => item.type === 'page' && item.url === 'https://localhost/');
    if (!page) {
      console.error('Fair Spin page not found');
      process.exit(1);
    }
    const socket = new WebSocket(page.webSocketDebuggerUrl);
    socket.addEventListener('open', () => {
      socket.send(JSON.stringify({
        id: 1,
        method: 'Runtime.evaluate',
        params: { expression, returnByValue: true, awaitPromise: true }
      }));
    });
    socket.addEventListener('message', event => {
      const message = JSON.parse(event.data);
      if (message.id !== 1) return;
      socket.close();
      if (message.error || message.result.exceptionDetails) {
        console.error(JSON.stringify(message.error || message.result.exceptionDetails));
        process.exit(1);
      }
      const result = message.result.result;
      console.log(typeof result.value === 'string' ? result.value : JSON.stringify(result.value));
    });
  });
}).on('error', error => {
  console.error(error.message);
  process.exit(1);
});
