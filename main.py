from livereload import Server, shell


server = Server()
server.watch('dist',)
server.serve(default_filename='dist/index.html')
