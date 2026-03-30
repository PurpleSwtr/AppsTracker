import webview

def say_hello():
    print("Hello from JavaScript!")

window = webview.create_window('Python Webview Demo', js_api=say_hello)
webview.start()
