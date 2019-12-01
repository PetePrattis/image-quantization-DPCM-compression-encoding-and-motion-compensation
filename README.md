# A Python Program / Project

**This is a Python project from my early days as a Computer Science student**

_This programs were created for the sixth semester class Multimedia Systems
and are projects for extra credit for the class_

> #### Description of project
>
>>A series of Python scripts that implement some multimedia compression functions and actions.
>

> #### Steps of project
>
> 1. Read the image and quantize the input panel using the quantization parameter
> 2. Εncode the number of repetitions of the quantized pixel table by first recording the location where a new color occurs and only recording when a new color appears
> 3. Οrganize the resulting structure and store it effectively
> 4. Reading a video sequence
> 5. Calculation of the different sequential frames, pixel by pixel
> 6. The differences have a lower entropy - quantization of the values as determined by the value of the quantization parameter given at the input
> 7. As an input you should be able to accept any character sequence
> 8. You should be able to set the dictionary size as an input Assume a maximum size of 256 (8-bytes)
> 9. At the output should be a list of indexes corresponding to the input string taking into account the dictionary-index word pairs.
> 10. Give the output a number that expresses the compression ratio
> 11. Perform a procedure that accepts two frames as input and calculates their difference and returns an error frame, no motion vector is calculated
> 12. Implement a function that accepts two frames, a reference frame that will be used when searching for motion vectors, and a target frame that will be provided. Divide the target frame into 16 X 16 macroblock blocks, and if the width and height of the frame are not multiples of 16, fill the frame with black pixels appropriately. For each block in the target box, refer to the corresponding position in the reference box and find the area that gives the best result. Use metric SAD in the resulting search area for k = 16 so that the motion vectors are sized to a maximum of 16 pixels in each direction. Based on the prediction block calculate the error block as the difference between the original block and the predicted one. This process will result in an error frame when all blocks are completed.

> #### About this project
>
> - The comments to make the code understandable, are within the .py archive
> - This project was written in IDLE, Python’s Integrated Development and Learning Environment.
> - This program runs for Python version 2.7
> - This repository was created to show the variety of the work I did and experience I gained as a student
>

