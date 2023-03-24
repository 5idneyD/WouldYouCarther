# ReactPy

This is a boilerplate dir structure that allows you to build a webapp using Flask and React.

You can write all you React code in the src/index.js file, which is then called into the templates/index.html file.
You will then need to transpile this index.html file so that the react code is readbale by the browser.
I am using esbuild to do this. Originally, webpack was used, however it was replaced with esbuild due to no need for configurations and being much faster.

The Python backendusing Flask is written in the app.py file in the root directory.

To run the web app, you simply need to run `npm run dev`

This will transpile the react code and save the new file in the dist directory. The flask backend will then call the files from the dist directory.
Using `npm run dev`, both the flask file and react are hot re-loaded, meaning if they change, either the flask backe-end will be re-started, or the react code will be re-transpiled automatically.

When you are ready to deploy the app, the final command you need to run is `npm run build`.
This will compile & optimize all react files and minify css files, and save them in the dist dir.
