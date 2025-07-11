import socket
import time
import random
import sys
import threading

# === Twitch Bot Account Info ===
NICK = "your_bot_username"
PASS = "oauth:your_oauth_code"
HOST, PORT = "irc.chat.twitch.tv", 6667

# === Default Welcome Message ===
welcome_message = "Alarm WELCOME {user} TO THE MUGA THON!!! Alarm ENJOY THE MUGA THON o7"

# === Funny loading quotes ===
funny_lines = [
    "MUGA", "are you gonna use this right? ;)", "MADE BY YOBOIYEETER/LGMBRYDAN!!",
    "I like you have a cupcake!", "who ya watching?", "are ya winnin son?",
    "OMG ITS YOU!! HI!!", "what's good", "wsp", "yo", "hello", "hi", "welcome to my thing"
]

# === Loading screen animation ===
def loading_animation():
    percent = 0
    while percent < 100:
        percent = min(percent + 7, 100)
        bar = '=' * (percent // 7)
        space = ' ' * ((100 - percent) // 7)
        sys.stdout.write(f"\r[{bar}{space}] {percent}%  ")
        sys.stdout.flush()
        print(f"  {random.choice(funny_lines)}")
        time.sleep(0.2)
    print("\n✅ Loading complete!\n")

# === Send a message ===
def send_message(sock, msg, channel):
    sock.send(f"PRIVMSG {channel} :{msg}\r\n".encode())

# === Parse incoming IRC messages ===
def parse_irc_message(raw):
    tags = {}
    username = ""
    message = ""

    try:
        if raw.startswith("@"):
            tag_part, rest = raw[1:].split(" ", 1)
            for pair in tag_part.split(";"):
                if "=" in pair:
                    key, value = pair.split("=", 1)
                    tags[key] = value

            if "!" in rest and "PRIVMSG" in rest:
                prefix, msg_part = rest.split(" PRIVMSG ", 1)
                username = prefix.split("!")[0]
                message = msg_part.split(":", 1)[1]
    except Exception as e:
        print(f"Error parsing IRC message: {e}")

    return tags, username, message

# === Connection setup ===
def connect(channel):
    sock = socket.socket()
    sock.connect((HOST, PORT))
    sock.send(f"PASS {PASS}\r\nNICK {NICK}\r\nJOIN {channel}\r\n".encode())
    print(f"✅ Connected to {channel} as {NICK}")
    return sock

# === Input thread for sending messages from terminal ===
def chat_input_loop(sock, channel):
    while True:
        try:
            msg = input()
            if msg.lower() == "/exit":
                print("👋 Exiting input loop...")
                break
            if msg.strip():
                send_message(sock, msg, channel)
        except KeyboardInterrupt:
            break

# === Bot chat logic ===
def run_bot(channel):
    sock = connect(channel)
    buffer = ""

    # Start input thread
    input_thread = threading.Thread(target=chat_input_loop, args=(sock, channel), daemon=True)
    input_thread.start()

    while True:
        try:
            buffer += sock.recv(2048).decode()
            lines = buffer.split("\r\n")
            buffer = lines.pop()

            for line in lines:
                if not line:
                    continue

                if line.startswith("PING"):
                    sock.send("PONG :tmi.twitch.tv\r\n".encode())
                    continue

                if "PRIVMSG" in line:
                    tags, username, message = parse_irc_message(line)

                    if tags.get("first-msg") == "1":
                        msg = welcome_message.replace("{user}", username.upper())
                        send_message(sock, msg, channel)

                    print(f"{username}: {message}")

        except (socket.error, ConnectionResetError):
            print("⚠️ Connection lost. Reconnecting in 5 seconds...")
            time.sleep(5)
            sock = connect(channel)
            buffer = ""

# === Main Menu ===
def main_menu():
    global welcome_message

    # Credit message at the top
    print("\n🎉 Special thanks to 2xkumaking who inspired me.. basically who created it all.")
    print("Alarm FIRST TIME CHATTER! Alarm WELCOME! LETSGO MUGA THON\n")

    while True:
        print("=== MUGA THON BOT MENU ===")
        print("1. Start Bot")
        print("2. Set Welcome Message")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            raw_channel = input("Enter Twitch channel to connect to (no #): ").strip().lower()
            channel = f"#{raw_channel}"
            print("\n🔄 Starting bot...")
            loading_animation()
            run_bot(channel)

        elif choice == "2":
            print("\nType your custom welcome message.")
            print("Use {user} where you want the username to appear.")
            custom = input("New welcome message: ").strip()
            if "{user}" not in custom:
                print("⚠️ You must include {user} in your message!")
            else:
                welcome_message = custom
                print("✅ Welcome message saved!")

        elif choice == "3":
            print("👋 Exiting. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please choose 1, 2, or 3.")

# === Start ===
if __name__ == "__main__":
    main_menu()
