# furulab2022hackathon_ramen
Collect and geo-reference content including unarchived satellite and drone imagery footage, 3D data, and other content related to Russia's progress in Ukraine.

## members
* [Ibuki Shibayama](https://github.com/ibuki76)  
* [Sota Suzuki](https://github.com/SotaSuzuki-1327)
* [Yasuda Haruka](https://github.com/halgraphic)
* [Shogo Hirasawa](https://github.com/ShogoHirasawa)

## Automated-credit-input Script

### background:  
When geo-referencing, some images need to be clearly credited. Since it was time-consuming to use image-editing software to credit each image one by one, we created a Python script to do it.

### How to use:  
- Put any string of your own in the following place

```
output_image.text((3115 ,440),"hogehogehogehogehoge", fill=(0, 0, 0),)
```

- Then run the script. After execution, you will be taken to the file selection screen. It is possible to select multiple files at the same time.

<img width="796" alt="スクリーンショット 2022-10-04 9 28 22" src="https://user-images.githubusercontent.com/29940264/193709191-4e6a6fd0-c09f-40b4-b224-3ab41665e06a.png">

- After selection, the file will be saved as "new_*" in the directory where the script was executed.
The "*" will be the name of the original file.

<img width="1047" alt="image (4)" src="https://user-images.githubusercontent.com/29940264/193709654-f4ff982e-16d9-4d44-8c70-6beec70be8b0.png">


### Upcoming updates
- Since the text input position is specified in absolute coordinates, it should be specified in relative coordinates. Even if the image size ratio is different, the text should be inserted at the same location.

- This has only been tested in a MacOS environment, so it needs to be verified in Windows as well.

- Font adjustment.

