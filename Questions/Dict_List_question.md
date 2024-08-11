1. **Nested Dictionaries and Lists:**
   Describe a scenario where you have a dictionary containing lists, and within those lists, there are dictionaries. Ask about accessing and modifying specific elements within this nested structure.

   Example:
   Given a dictionary `employee_data` containing lists of employee information, where each employee's information is represented as a dictionary, how would you update the salary of the employee with ID 101?

   ```python
   employee_data = {
       'employees': [
           {'id': 101, 'name': 'John', 'salary': 50000},
           {'id': 102, 'name': 'Alice', 'salary': 60000},
           {'id': 103, 'name': 'Bob', 'salary': 55000}
       ]
   }
   ```

   Constraints: IDs are unique, employee data is not sorted.

2. **Sorting and Filtering:**
   Present a dictionary containing lists of numbers and ask to sort the numbers within each list and filter out the lists that contain numbers less than a certain threshold.

   Example:
   Given the dictionary `data`, containing lists of integers, sort the numbers within each list in ascending order and remove lists that have maximum values less than 50.

   ```python
   data = {'list1': [30, 40, 20], 'list2': [80, 10, 60], 'list3': [70, 90, 100]}
   ```

   Constraints: Lists may contain duplicate integers, lists may vary in length.

3. **Aggregation and Calculation:**
   Provide a dictionary representing students and their test scores. Ask for the average score of students whose names start with a vowel.

   Example:
   Given the dictionary `student_scores`, compute the average test score of students whose names start with a vowel.

   ```python
   student_scores = {'Alice': [80, 90], 'Bob': [75, 85], 'Eve': [95, 85]}
   ```

   Constraints: Names are case-sensitive, students may have varying numbers of test scores.

4. **Combining Multiple Dictionaries:**
   Describe a scenario where there are multiple dictionaries representing different aspects of data (e.g., student grades, attendance, and extracurricular activities). Ask about combining these dictionaries to generate a comprehensive report.

   Example:
   Given dictionaries `grades`, `attendance`, and `activities`, combine them to generate a report showing the average grade of each student, their attendance percentage, and the number of extracurricular activities they participate in.

   ```python
   grades = {'Alice': 85, 'Bob': 90, 'Eve': 88}
   attendance = {'Alice': 90, 'Bob': 95, 'Eve': 92}
   activities = {'Alice': 3, 'Bob': 2, 'Eve': 4}
   ```

   Constraints: Dictionaries have the same keys, values represent different aspects of student performance.

5. **Searching and Updating:**
   Present a dictionary containing lists of tuples representing product details. Ask to search for a specific product by name and update its price.

   Example:
   Given the dictionary `products`, find the product named "Laptop" and update its price to $1200.

   ```python
   products = {'Electronics': [('Phone', 800), ('Laptop', 1000), ('Tablet', 500)]}
   ```

   Constraints: Products have unique names, prices are integers, product categories are predefined.

6. **Sparse Matrix Representation:**
   Describe a scenario where a matrix is represented as a dictionary of dictionaries. Ask about operations like matrix addition, multiplication, or finding the transpose.

   Example:
   Given dictionaries `matrix1` and `matrix2`, representing sparse matrices, perform addition of the matrices.

   ```python
   matrix1 = {0: {0: 3, 2: 2}, 1: {1: 4}}
   matrix2 = {0: {0: 1, 1: 2}, 2: {2: 3}}
   ```

   Constraints: Matrices may be sparse, keys represent row and column indices.

7. **Graph Representation:**
   Describe a graph represented as a dictionary where keys are nodes and values are lists of adjacent nodes. Ask about traversing the graph or finding shortest paths.

   Example:
   Given the dictionary `graph`, representing a graph, find the shortest path from node 'A' to node 'F'.

   ```python
   graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D', 'E'], 'D': ['F'], 'E': ['F']}
   ```

   Constraints: Graph may be directed or undirected, nodes are unique.

8. **Data Cleaning and Transformation:**
   Describe a scenario where a dictionary contains messy data that needs cleaning and transformation. Ask about techniques for data normalization or filtering.

   Example:
   Given the dictionary `data`, containing messy data with inconsistent formatting, clean and transform it into a standardized format.

   ```python
   data = {'Alice': '$50,000', 'Bob': '60000', 'Eve': '55K'}
   ```

   Constraints: Data may contain missing values, inconsistent units, or non-numeric characters.

9. **Grouping and Aggregation:**
   Describe a dataset represented as a dictionary of dictionaries where keys represent categories and values contain data points. Ask about grouping the data by category and computing statistics for each group.

   Example:
   Given the dictionary `sales_data`, containing sales figures for different products and regions, group the data by product category and compute the total sales for each category.

   ```python
   sales_data = {'Electronics': {'TV': 5000, 'Phone': 8000}, 'Clothing': {'Shirt': 2000, 'Pants': 3000}}
   ```

   Constraints: Categories and products are predefined, sales figures are integers.

10. **Time Series Analysis:**
    Describe a scenario where data is organized as a dictionary with timestamps as keys and values representing observations. Ask about operations like calculating moving averages or detecting trends.

    Example:
    Given the dictionary `temperature_data`, containing temperature readings for different dates, compute the 7-day moving average for temperature.

    ```python
    temperature_data = {'2022-01-01': 25, '2022-01-02': 28, '2022-01-03': 30, ...}
    ```

    Constraints: Timestamps are in chronological order, temperature readings are integers.

11. **Sparse Vector Operations:**
    Describe a scenario where vectors are represented as dictionaries with indices as keys and values as non-zero elements. Ask about operations like vector addition, dot product, or normalization.

    Example:
    Given dictionaries `vector1` and `vector2`, representing sparse vectors, compute their dot product.

    ```python
    vector1 = {0: 3, 1: 0, 2: 4}
    vector2 = {0: 1, 2: 2, 3: 5}
    ```

    Constraints: Vectors may contain non-zero elements only at

 certain indices.

12. **Combining Lists and Dictionaries:**
    Describe a scenario where lists of dictionaries represent records in a database. Ask about querying, filtering, or aggregating data based on specific criteria.

    Example:
    Given a list of dictionaries `employees`, containing employee records, find all employees with a salary greater than $50000.

    ```python
    employees = [{'name': 'Alice', 'salary': 60000}, {'name': 'Bob', 'salary': 55000}, ...]
    ```

    Constraints: Employee records may contain additional fields, such as department or hire date.

13. **Sparse Representation of Text Data:**
    Describe a scenario where text documents are represented as dictionaries with words as keys and frequencies as values. Ask about operations like similarity calculation or topic modeling.

    Example:
    Given dictionaries `document1` and `document2`, representing word frequencies in text documents, compute their cosine similarity.

    ```python
    document1 = {'apple': 3, 'banana': 2, 'orange': 1}
    document2 = {'apple': 1, 'banana': 2, 'mango': 4}
    ```

    Constraints: Words are case-sensitive, documents may vary in length.

14. **Geospatial Data Analysis:**
    Describe a scenario where geospatial data is represented as a dictionary with coordinates as keys and attributes as values. Ask about operations like finding nearest neighbors or clustering.

    Example:
    Given the dictionary `locations`, containing latitude and longitude coordinates of points of interest, find the nearest point to a given location.

    ```python
    locations = {(40.7128, -74.0060): 'New York', (34.0522, -118.2437): 'Los Angeles', ...}
    ```

    Constraints: Coordinates are in decimal degrees, points may be distributed unevenly.

15. **Network Traffic Analysis:**
    Describe a scenario where network traffic data is represented as a dictionary with IP addresses as keys and traffic volumes as values. Ask about detecting anomalies or identifying patterns.

    Example:
    Given the dictionary `traffic_data`, containing traffic volumes for different IP addresses, detect IP addresses with unusually high traffic.

    ```python
    traffic_data = {'192.168.0.1': 10000, '192.168.0.2': 5000, '192.168.0.3': 15000, ...}
    ```

    Constraints: IP addresses are unique, traffic volumes are integers.

16. **Inventory Management:**
    Describe a scenario where inventory data is represented as a dictionary with product IDs as keys and quantities as values. Ask about operations like restocking, depletion, or forecasting.

    Example:
    Given the dictionary `inventory`, containing quantities of different products in stock, predict the total quantity of products in stock after a week, assuming constant depletion rates.

    ```python
    inventory = {'product1': 100, 'product2': 200, 'product3': 150, ...}
    ```

    Constraints: Product IDs are unique, quantities may vary over time.

17. **Genetic Sequence Analysis:**
    Describe a scenario where genetic sequences are represented as dictionaries with nucleotides as keys and frequencies as values. Ask about operations like sequence alignment or mutation detection.

    Example:
    Given dictionaries `sequence1` and `sequence2`, representing DNA sequences, compute their Hamming distance.

    ```python
    sequence1 = {'A': 10, 'C': 20, 'G': 15, 'T': 5}
    sequence2 = {'A': 10, 'C': 25, 'G': 15, 'T': 5}
    ```

    Constraints: Nucleotides are case-sensitive, sequences may vary in length.

18. **Game State Representation:**
    Describe a scenario where game states are represented as dictionaries with player positions, scores, or other attributes. Ask about operations like move validation or AI decision making.

    Example:
    Given the dictionary `game_state`, representing the state of a chess game, validate a proposed move and update the game state accordingly.

    ```python
    game_state = {'player1': {'king': (1, 1), 'queen': (1, 2), ...}, 'player2': {'king': (8, 8), ...}}
    ```

    Constraints: Game rules are predefined, players may have different pieces.

19. **Sensor Data Processing:**
    Describe a scenario where sensor data is represented as dictionaries with timestamps as keys and sensor readings as values. Ask about operations like outlier detection or trend analysis.

    Example:
    Given the dictionary `sensor_data`, containing temperature readings over time, detect outliers and remove them from the dataset.

    ```python
    sensor_data = {'2022-01-01 00:00:00': 25, '2022-01-01 00:01:00': 30, ...}
    ```

    Constraints: Timestamps are in chronological order, sensor readings are numerical.

20. **Financial Portfolio Analysis:**
    Describe a scenario where financial data is represented as dictionaries with asset names as keys and prices or quantities as values. Ask about operations like portfolio optimization or risk assessment.

    Example:
    Given dictionaries `portfolio` and `market_data`, representing the current portfolio and market prices of assets, compute the total value of the portfolio and assess its risk.

    ```python
    portfolio = {'stock1': 100, 'bond1': 200, 'commodity1': 150, ...}
    market_data = {'stock1': 50, 'bond1': 150, 'commodity1': 100, ...}
    ```

    Constraints: Asset names are unique, prices and quantities are numerical.