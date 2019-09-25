# Steps to reproduce
1. Create repository on GitHub
2. Clone repository
    ```
    git clone https://github.com/Aenorieg/LearningPython.git
    ```
3. Create circumference.py file
    1. define pi = 3.14159
    1. define radius = 3
4. Create areaCode.py file
    1. install regular expressions
        ````
        install re
        ````
     1. use regular expressions to extract area code
        ````
        match = re.search(r'^\d{0,3}', phone)
        ````
5. Make a data directory 
    ````
    mkdir data
    ````
6. Download Homo_sapiens.GRCh37.75.gtf.gz file in data directory
    1. download wget
        ````
        brew install wget
        ````
    1. download Homo_sapiens.GRCH37.75.gtf.gz
        ````
        wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz
        ````
7. Unzip Homo_sapiens.GRCh37.75.gtf.gz file
    ````
    gunzip Homo_sapiens.GRCh37.75.gtf.gz file
    ````
8. Verify that the start of the file
    ````
    head ~/data/Homo_sapiens.GRCh37.75.gtf
    ````
    is:
     ````
     #!genome-build GRCh37.p13
     ````
9. Create a gene_names.py file
    1. use regular expressions for gene_name
        ````
        gene_name\s\"(.*?)\";
        ````
    1. use regular expressions for chromosome
        ````
        ^(.*?)\t
        ````
    1. use regular expressions for starting_position
        ````
        \t(\d*?)\t
        ````
    1. use regular expressions for ending_position
        ````
        \t\d*\t(\d*?)\t
        ````
    1. JSON format
        ````
        gene_array.append({"geneName": gene_name, "chr": chromosome, "startPos": int(starting_position),
                           "endPos": int(ending_position)})
        ````
    1. run file in LearningPython directory
        ````
        ./gene_names.py data/Homo_sapiens.GRCh37.75.gtf
        ````
10. Commit and push changes to GitHub
    1. for circumference.py
        ````
        git add circumference.py
        git commit -m "Adding circumference file"
        git push
        ````
    1. for areaCode.py
        ````
        git add areaCode.py
        git commit -m "Adding areaCode file"
        git push
        ````
    1. for gene_names.py
        ````
        git add gene_names.py
        git commit -m "Adding gene names file"
        git push
        ````
    1. for data
        1. download and install the Git command line extension
            ````
            git lfs install
            ````
        1. manage Homo_sapiens.GRCh37.75.gtf
            ````
            git lfs track "*.gtf"
            ````
        1.  add and commit .gitattributes
            ````
            git add .gitattributes
            git commit -m "Adding git attributes to track big file"
            ````
        1. add and commit data
            ````
            git add data/
            git commit -m "Adding big data file"
            git push
            ````

