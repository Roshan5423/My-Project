# My-Project
Driver Drowsiness Detection 

Driver drowsiness detection is a project built using Dlib and OpenCV with Python as a backend language.

Logic of project -
The project includes direct working with the 68 facial landmark detector and also the face detector of the Dlib library. The 68 facial landmark detector is a robustly trained efficient detector which detects the points on the human face using which we determine whether the eyes are open or they are closed.

The working of the project -
1 . As you can see the above screenshot where the landmarks aredetected using the detector.
2 . Now we are taking the ratio which is described as 'Sum of distances of vertical landmarks divided by twice the distance between horizontal landmarks'.
3 . Now this ratio is totally dependent on your system which you may configure accordingly for the thresholds of sleeping, drowsy, active.

![Active](https://user-images.githubusercontent.com/112264930/187746037-7047db33-95f2-433b-a55a-67e041152961.png)

![Drowsy](https://user-images.githubusercontent.com/112264930/187746073-7a3b1342-8309-4262-bd6f-10829beaafdf.png)

![Yawning](https://user-images.githubusercontent.com/112264930/187746097-ed979fce-91ff-45f2-a90a-fe35964ce2ef.png)





