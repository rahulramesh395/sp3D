#!/bin/bash
echo $HOME
cd /home/pi/sp3D/web_api/web/sp3d_app
sudo npm run dev -- --port 3000 --host
