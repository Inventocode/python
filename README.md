## 使用说明

### 安装 RPi.GPIO 和 gpiozero 库
    pip install RPi.GPIO
    pip install gpiozero

### 安装mpg123和fswebcam
    sudo apt-get update
    sudo apt-get install mpg123
    sudo apt-get install fswebcam
### 下载并解压
    wget https://github.com/Inventocode/raspberry-pi-traffic-light/archive/refs/heads/main.zip
    unzip -d traffic-light main.zip
    rm main.zip
### 运行
    cd traffic-light
    python main.py

配置在main.py 5~24行