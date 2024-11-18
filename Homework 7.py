#Jorge Corona
#Computer Science 1800 - Lab 7
#November 17, 2024
#Professor N. Kounavelis

def create_web_page():
    #Name and description
    name = input("Enter your name: ")
    description = input("Describe yourself: ")

    #HTML content
    html_content = f"""
    <html>
        <head>
            <title>{name}'s Personal Web Page</title>
        </head>
        <body>
            <center>
                <h1>{name}</h1>
            </center>
            <hr />
            <p>{description}</p>
            <hr />
        </body>
    </html>
    """

    #Content
    with open("personal_web_page.html", "w") as file:
        file.write(html_content)

    print("Web page created! Open 'personal_web_page.html' to view it.")

#Generate the web page
create_web_page()
