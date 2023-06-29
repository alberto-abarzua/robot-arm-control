#include <errno.h>
#include <fcntl.h>
#include <sys/types.h>
#include <unistd.h>
#include <cstring>
#include <iostream>
#include "config.h"
#include "messages.h"

/**
 * @brief ArmClient class, This class is used to create a TCP socket to
 * comunicate with the python controller This is completely independent from the
 * rest of the code, this is portion is going to be reprogramed for the esp32
 * version of the arm
 *
 */
class ArmClient {
   private:
    int clientSocket;
    int start_socket();

   public:
    ArmClient();

    ~ArmClient();

    int send_message(Message *msg);

    int receive_message(Message **msg);

    int setup();

    void stop();
};
