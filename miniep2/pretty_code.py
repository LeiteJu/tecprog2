def main():

    if len(sys.argv) < 2:
        
        print ("Missin argument")
        print ("Usage:")
        print ("python3 server.py <port>")
        exit(0)

    PORT = int (sys.argv[1])
    HOST = str(get_ip()) # localhost

    global users, clients
    global server_socket, heartbeat_socket
    global users_thread
    global END
    
    if len(sys.argv) == 3 and sys.argv[2] == "-v":
        global DEBUG
        DEBUG  = True

    last_success = last_exec()

    # write at the log file

    if last_success: #if last execution finished
        write_log(get_time() + "servidor iniciado - última execução finalizada com sucesso")
    else:
        write_log(get_time() + "servidor iniciado - última execução finalizada com falha")

    # get the users information from the file
    users = read_users()    

    users_thread = th.Thread(target=update_users)
    users_thread.start()

    signal.signal(signal.SIGTERM, quit)

    server_socket.bind((HOST, PORT))
    server_socket.listen()

    heartbeat_socket.bind((HOST, HEARTBEAT_PORT))
    heartbeat_socket.listen()