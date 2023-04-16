import React from 'react';
import ReactDOM from 'react-dom';
import * as ReactDOMClient from 'react-dom/client';

function App() {
  return (
    <div>
      <h2><u>This is a Flask and React boilerplate template</u></h2>
      <h2>This may not be the best layout or as good as create-react-app, but it includes my favourite build tools  and I hope it can help someone else
      </h2>
      <h2>Tools included in this boilerplate include</h2>
      <ul>
        <li>Flask (Python microframework)</li>
        <li>React.js as an optional frontend framework</li>
        <li>You can use vanilla js if preferred</li>
        <li>Vanilla CSS (mobile and desktop files are seperate)</li>
        <li>Esbuild to transpile all static files (this can be configured)</li>
        <li>Hot reloads when running "npm run dev"</li>
        <li>If your project is ready for deployment, run "npm run build", then "python app.py"</li>
      </ul>
      <h2>If you have any questions, leave them at <a href="https://github.com/5idneyD/ReactPy">5idneyD</a></h2>
    </div>
  )
}

const container = document.getElementById('root');
const root = ReactDOMClient.createRoot(container);
root.render(<App />);