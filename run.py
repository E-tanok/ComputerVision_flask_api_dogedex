from dogs_identification import app
from context import datasources_application, templates_path
from functions import class_my_files

if __name__ == "__main__":
    L_pictures = []
    dogs_data_path = datasources_application
    dict_extensions_files = class_my_files(dogs_data_path)
    L_pictures = dict_extensions_files['jpg']
    print(L_pictures)

    print("ecriture du fichier html contenant les images de chiens : ")
    f = open(templates_path+'dogs_list.html', 'w')
    f.write("{% extends 'index.html' %}\n{% block content %}\n")
    for picture in L_pictures:
        print(picture)
        html_string = "<option value=\"%s\">"%picture
        f.write(html_string)
        f.write("\n")
    f.write("{% endblock %}")
    f.close()
    app.run(debug=True)
