import subprocess, time, os, sys, json
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencv-python'])
try:
    os.system('cls')
except:
    try:
        os.system('clear')
    except:
        pass
try:
  with open("config.json", "r") as config:
    config = json.load(config)
except:
  print("config.json file is missing. Make sure you downloaded all the files and config is in the same folder")
  time.sleep(5)
  print("Exiting...")
  time.sleep(0.3)
  quit()
storage = []
price = config['price']
import pyautogui
print("Started")
while True:
  image = pyautogui.locateCenterOnScreen('assets/image.png', confidence = 0.9)
  if image:
    time.sleep(0.1)
    pyautogui.moveTo(image)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(1)
    imageone = pyautogui.locateCenterOnScreen('assets/image1.png', confidence = 0.9)
    if imageone:
      time.sleep(0.1)
      pyautogui.moveTo(imageone)
      time.sleep(0.1)
      pyautogui.click()
      time.sleep(0.1)
      imageone = pyautogui.locateCenterOnScreen('assets/image1.png', confidence = 0.9)
      if imageone:
        time.sleep(0.1)
        pyautogui.moveTo(imageone)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)
        imageone = pyautogui.locateCenterOnScreen('assets/image1.png', confidence = 0.9)
        if imageone:
            time.sleep(0.1)
            pyautogui.moveTo(imageone)
            time.sleep(0.1)
            pyautogui.click()
            time.sleep(0.1)
            imageone = pyautogui.locateCenterOnScreen('assets/image1.png', confidence = 0.9)
            if imageone:
              time.sleep(0.1)
              pyautogui.moveTo(imageone)
              time.sleep(0.1)
              pyautogui.click()
              time.sleep(0.1)
              imageone = pyautogui.locateCenterOnScreen('assets/image1.png', confidence = 0.9)
              if imageone:
                time.sleep(0.1)
                pyautogui.moveTo(imageone)
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(0.1)
                imageone = pyautogui.locateCenterOnScreen('assets/image1.png', confidence = 0.9)
                if imageone:
                  time.sleep(0.1)
                  pyautogui.moveTo(imageone)
                  time.sleep(0.1)
                  pyautogui.click()
                  time.sleep(0.1)
                  imageone = pyautogui.locateCenterOnScreen('assets/image1.png', confidence = 0.9)
                  if imageone:
                    time.sleep(0.1)
                    pyautogui.moveTo(imageone)
                    time.sleep(0.1)
                    pyautogui.click()
                    time.sleep(0.1)
                    imageone = pyautogui.locateCenterOnScreen('assets/image1.png', confidence = 0.9)
                    if imageone:
                      time.sleep(0.1)
                      pyautogui.moveTo(imageone)
                      time.sleep(0.1)
                      pyautogui.click()
                      time.sleep(0.1)
                      imageone = pyautogui.locateCenterOnScreen('assets/image1.png', confidence = 0.9)
                      if imageone:
                        time.sleep(0.1)
                        pyautogui.moveTo(imageone)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(0.1)
                        imageone = pyautogui.locateCenterOnScreen('assets/image1.png', confidence = 0.9)
                        if imageone:
                          time.sleep(0.1)
                          pyautogui.moveTo(imageone)
                          time.sleep(0.1)
                          pyautogui.click()
                          time.sleep(0.1)
                          imageone = pyautogui.locateCenterOnScreen('assets/image1.png', confidence = 0.9)
                          if imageone:
                            time.sleep(0.1)
                            pyautogui.moveTo(imageone)
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(0.1)
                            imageone = pyautogui.locateCenterOnScreen('assets/image1.png', confidence = 0.9)
                            if imageone:
                              time.sleep(0.1)
                              pyautogui.moveTo(imageone)
                              time.sleep(0.1)
                              pyautogui.click()
                              time.sleep(0.1)
                              imagetwo = pyautogui.locateOnScreen('assets/image2.png', confidence = 0.9)
                              if imagetwo:
                                time.sleep(0.1)
                                pyautogui.moveTo(imagetwo)
                                time.sleep(0.1)
                                pyautogui.click()
                                time.sleep(1)
                                imagethree = pyautogui.locateCenterOnScreen('assets/image3.png', confidence = 0.9)
                                if imagethree:
                                  pyautogui.moveTo(imagethree)
                                  time.sleep(0.1)
                                  pyautogui.click()
                                  time.sleep(0.1)
                                  pyautogui.write(f"{price}")
                                  time.sleep(0.1)
                                  pyautogui.press('enter')
                                  time.sleep(0.1)
                                  imagefour = pyautogui.locateCenterOnScreen('assets/image4.png', confidence = 0.9)
                                  if imagefour:
                                    time.sleep(0.1)
                                    pyautogui.moveTo(imagefour)
                                    time.sleep(0.1)
                                    pyautogui.click()
                                    time.sleep(1)
                                    imagefive = pyautogui.locateCenterOnScreen('assets/image5.png', confidence = 0.9)
                                    if imagefive:
                                      pyautogui.moveTo(imagefive)
                                      time.sleep(0.1)
                                      pyautogui.click()
                                      time.sleep(0.1)
                                      print("Successful Restock!")
