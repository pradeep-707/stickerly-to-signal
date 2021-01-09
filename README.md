# Stickerly to Signal

Add sticker.ly packs to signal

## Installation

```bash
pip3 install signalstickers-client
```

```bash
pip3 install requests
```
> **You will need your Signal credentials** To obtain them, open the Developer
> Tools in Signal Desktop, and type `window.reduxStore.getState().items.uuid_id`
> to get your USER, and `window.reduxStore.getState().items.password` to get
> your PASSWORD.

+ Create `user-id.txt` and `password.txt` and paste the above into there.
+ Run main.py and type the stickerly ID of the pack you want to add.
+ Copy the link from newly created `packid_signal.txt` inside res to install it in signal.