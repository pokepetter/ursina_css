# Ursina CSS
Ursina CSS is a subset of ursina running in the browser. You are however limitied to only 2D and basics like entities, buttons and text.

When creating your game add the ``ursina`` and the ``Brython-<version>`` folders and the ``.nojekyll``, ``index.html`` and ``start_server.bat`` files in your root directory.
You can then simply code your game as a standard game and then open ``start_server.bat`` (*Windows*) or open your terminal, navigate to your game directory and run ``python3 -m http.server <port>``.
If you do not specify the port, it will be by default 8000.
You then just need to open your browser to ``localhost:<port>`` and enjoy.


Implemented Features:
 - [x] Entity
 - [x] Button
 - [x] Text
 - [x] camera
 - [x] color
 - [x] Sequence
 - [x] window
 - [x] mouse
 - [ ] raycast
 - [ ] rotation
 - [ ] Tilemap
