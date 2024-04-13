from flask import Flask, render_template    

app=Flask(__name__)


@app.route("/")
def index():
    """We are going to use render_template to return a a page with the help of Jinja2. Because of there will be lots of operations needs ot be done then 
    it is advisable to template rather than returning writing code for everything and returning for each iteration. 
    
    Additionally, you can define variables inside the code and can pass it over the template as shown below.
    
    Few filters form jinja2 will be used in this methods such as :
    safe - it is going to execute the html tags passed to the template. - Such as <strong> tag in below will bold as bold using sfe filter in template file
    capitalize - it going to convert the output in camel case
    lower - it going to convert the output to lower case
    upper - it going to convert the output to upper case
    title - it going to convert the output to title case
    trim - it going to trim the last space
    striptags - it is going to shred the html tags so that no html code will be executed. it is useful for securing app form hackers.
    
    

    Returns:
        template page: it will return and index.html page from defined templates. 
    """
    
    firstName='Ravi'
    stuff= "This is a <strong>Bold</strong> Statement"
    
    
    """
    Lets try loops in Jinja2: for this lets create a list here and then we will use for statement in index.html file and will iterate through each element of the list

    Returns:
        for loop : element of list
    """
    favoritePizza= ["Tandoori", "Cheese", "VegiDelight", "Mushroom", 41]



    
    return render_template("index.html",
                           firstName=firstName,
                           stuff=stuff,
                           favoritePizza=favoritePizza)

@app.route("/users/<name>")
def users(name):
    """Ones server will receive user API request it will pass that information to user.html and will render the output.
    above API will take input from user via URL. The name passed from URL will stored in tag <name> and that will be passed to name in users functions. 
    While returning the template in this function name will passed to template with variable username and final output will start rendering on web.

    Args:
        html page: this request will give user.html template out
    """
    return render_template("user.html", user_name=name)



@app.errorhandler(404)
def pageNotFound(e):
    """creating a custom error page. whenever user request for something which is not in application or misspelled something which is not available
    server will throw 404 error that wil be captured by pageNotFound function.

    Args:
        e (404): error type 404 - page not found

    Returns:
        html page: a custom error page for 404 error page not found from templates folder
    """
    return render_template("404.html"), 404
