#include <stdio.h>
#include <string.h>

void send_message() {
  // Define our message
  char message[] = "{\"text\": \"This is a response message\"}";
  // Collect the length of the message
  unsigned int len = strlen(message);
  // We need to send the 4 bytes of length information
  printf("%c%c%c%c", (char) (len & 0xFF),
                     (char) ((len>>8) & 0xFF),
                     (char) ((len>>16) & 0xFF),
                     (char) ((len>>24) & 0xFF));
  // Now we can output our message
  printf("%s", message);
}

void read_message() {
  
}

int main(int argc, char* argv[]) {
  read_message();
  send_message();
  return 0;
}