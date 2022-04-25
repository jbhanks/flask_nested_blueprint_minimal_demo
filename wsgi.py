from myapp import create_app

app = create_app()

# Uncomment if serving to web
#if __name__ == "__main__":
        #app.run(host='0.0.0.0', port=5002, debug=True)

# Keep if testing locally
if __name__ == "__main__":
        app.run(host='127.0.0.1', port=5002, debug=True)

