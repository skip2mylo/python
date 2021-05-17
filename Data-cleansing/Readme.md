# Books Data Cleansing strategies:

1. Drop all columns that do not relate to our analysis requirement.
	Columns interested:
	- A graph over the publication years. *'Date of Publication'
	- Number of books per author. *'Author'
	- make a graph that show the number of books in each city. *'Place of Publication'

2. Fillout the NaN in interested columns.
	- Fillout 1778 NaN in 'Author' column to 'Unkown' 
	It will benifit the cleansing section happend later, and also keep the data integrity. 
	- Skipped filling out 178 NaN in 'Date of Publication' 
	It is acceptable to eliminate a small number of data here to keep the result clean and correct.

3. Cleanse 'Date of Publication' column.
	- Use an regression expression to extract first 4 digits from the column
	Most messy value in the columns are displayed as a start year and an end year, with [] or ?, simply just extract the first appeared 4 digits which is the proper year we need.
	- Convert datatype from string to numerical datatype.
	- Check the NaN value percentage after the cleanse (2%), totally acceptable

4. Cleanse 'Place of Publication' column.
	- No Null value in this column
	- Take a primary look at the dataset and 50 most frequently appeared city
	Found out London, Boston, Oxford are the city appeared the most and with some messy data.
	Also, some places have variants of having or not having '-' in the name
	- Extract 'London', 'Boston', 'Oxford' when the string contains these words
	Using np.where() function to find the key words and extract them.
	- Replace the '-' with a space, ' '.

5. Cleanse 'Author' column.
	- Take a look at the 50 authors that have the most books
	Found out 'Tennyson, Alfred Tennyson - Baron' and 'TENNYSON, Alfred - Baron Tennyson' are both on the list
	- Convert all the string to lower case. 
	This will solve the problem of same value with messy upper lower cases issue 
	- Remove contents after '-'(followed by usually a title or redundant content)
	Using a regress expression to find strings contains characters followed by a '-', replacing that part with ''. 

# Visulization strategies:

1. A graph over the publication years
	graph type: histogram
	Histogram represents the frequency of a value appeared. Every time we see an year in the row means there's a book published this year. We can say that the frequency of pulication year appeared means the number of book published. 
	I chose the bin to be ranged from 1500 to 1950 with an interval on 10 years, which could clearly elaborate the difference between decades to draw insight, for example, the publications of book boomed from 1850-60 and increased ever since.
2. Number of books per author
	graph type: horizontal bar
	*There are 4951 authors in the dataset. I don't think any graph will be able to reflect the requirement. So I decided to show a graph of the Top 10 authors that have written most books instead.
	Bar graph can elaborate the differences of numbers of books between authors in a straight forward way.

3. A graph that shows the number of books in each city
	graph type: horizontal bar
	*There are 1170 distinct cities in the dataset after cleansing. So I decided to make a graph that only shows the Top 10 cities that have the most books published instead.
	Again, bar graph is the neat and intuitive way to show differences between cities.

![](https://github.com/skip2mylo/junec-portfolio/blob/2e660decc08f0b61a9ad88aaee8b45788299cf64/images/Books%20published%20over%20years.png)
![](https://github.com/skip2mylo/junec-portfolio/blob/2e660decc08f0b61a9ad88aaee8b45788299cf64/images/Top%2010%20authors%20that%20wrote%20the%20most%20books.png)
![](https://github.com/skip2mylo/junec-portfolio/blob/2e660decc08f0b61a9ad88aaee8b45788299cf64/images/Top%2010%20cities%20that%20published%20most%20books.png)
