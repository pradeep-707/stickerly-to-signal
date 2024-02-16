# Stickerly to Signal

Add sticker.ly packs to signal

## Installation

```bash
pip3 install signalstickers-client
```

```bash
pip3 install requests
```
# Signal Desktop Credential Retrieval

To retrieve your Signal credentials, follow these steps:

1. **Using Signal Desktop App:**
   - Launch the Signal Desktop app.
   - Enable developer tools by running the Signal Desktop app with the flag `--enable-dev-tools`.
   - Alternatively, if you're using the Signal Desktop Beta app, open Developer Tools by navigating to "View" > "Open/Close Developers Tool".
   - Change the JavaScript context from "top" to "Electron Isolated Context".

2. **Retrieve Your User ID (USER):**
   - In the developer console, type:
     ```
     window.reduxStore.getState().items.uuid_id
     ```

3. **Retrieve Your Password:**
   - In the developer console, type:
     ```
     window.reduxStore.getState().items.password
     ```

+ Create `user-id.txt` and `password.txt` and paste the above into there.
+ Run main.py and type the stickerly ID of the pack you want to add.
+ Copy the link from newly created `packid_signal.txt` inside res to install it in signal.
