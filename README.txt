CP 8202: Advanced Software Engineering Project

Name: Malcolm Gomes
Student Number: 500680348

Please read the below before attempting to run the programs

To run the 3 micro-services:
1) Make sure Docker is installed
2) Navigate to the 'Alt' directory in the command line.
3) If you are running the microservices for the first time: run the command 'docker-compose up --build' 
   Else: just run the command 'docker-compose up'

Once the microservices are running you can test them with the Python program in the 'interface' directory
1) Make sure you have Python 3 installed 
2) Navigate to the 'interface' directory in the command line.
3) Run the command 'python main.py'
4) Wait for a few seconds for the program to start up.
5) You will be prompted for a URL to an image.
    I have images hosted for testing on my ryerson site.
    Sample Images:
    https://www.cs.ryerson.ca/~m24gomes/images/lion.jpg
    https://www.cs.ryerson.ca/~m24gomes/images/fox.jpg
    https://www.cs.ryerson.ca/~m24gomes/images/dog.jpg
    https://www.cs.ryerson.ca/~m24gomes/images/joe.jpg
    https://www.cs.ryerson.ca/~m24gomes/images/dancer.jpg
    https://www.cs.ryerson.ca/~m24gomes/images/aragorn.jpg
    https://www.cs.ryerson.ca/~m24gomes/images/frodo.jpg

    
    Enter one of those URLs or any URL that links to an image.

6) You will be asked to chose a model to run the image on.
    Enter 'c' for the classification model which will tell you what the image is.
    Enter 's' for the saliency mapper model which will return a heat map of the salient portions of the image and return it. 
    Enter 't' for the style transfer model which will then ask you for another URL to a style image
        You can use one of the 4 style image URLs shown below or feel free to pick your pattern (results may vary based on chosen pattern)
            Style Images:    
            https://www.cs.ryerson.ca/~m24gomes/images/picasso.jpg
            https://www.cs.ryerson.ca/~m24gomes/images/starry.jpg
            https://www.cs.ryerson.ca/~m24gomes/images/scream.jpg
            https://www.cs.ryerson.ca/~m24gomes/images/fulchun.jpg
        After you enter the style image URL, the model will generate the stylized image and will return it.

    The outputs of the saliency mapper and style transfer model will be saved in the 'outputs' directory. 
    The results of the models on the lion image are already saved in the outputs folder by default. 
    You can delete them and run the models on the same image and you will get the same result.

