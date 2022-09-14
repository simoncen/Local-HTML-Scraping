from bs4 import BeautifulSoup

# working with files
# open a file and read the content of that specific file
with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    # tags = soup.find('h5')  # find the first element only, print(tags)
    # courses_html_tags = soup.find_all('h5')  # find all the elements as a list
    # for course in courses_html_tags:
    #     print(course.text)

    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')