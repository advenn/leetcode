# import pandas as pd
#
# def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
#     managers = employee[employee['']]
# import pandas as pd
#
# # Sample data
# data = {
#     'id': [1, 2, 3, 4],
#     'name': ['Joe', 'Henry', 'Sam', 'Max'],
#     'salary': [70000, 80000, 60000, 90000],
#     'managerId': [3, 4, None, None]
# }
#
# # Create a DataFrame
# df = pd.DataFrame(data)
#
# # Merge the dataframe with itself on managerId
# merged_df = df.merge(df, left_on='id', right_on='managerId', suffixes=('_emp', '_mgr'))
#
# # Filter out rows where employee's salary is more than manager's salary
# result_df = merged_df[merged_df['salary_emp'] > merged_df['salary_mgr']]
#
# # Extract employee names and display
# result = result_df[['name_emp']]
# result.columns = ['Employee']
# print(result)
import pandas as pd

# Your provided data scheme
data = [
    [1, "Joe", 70000, 3],
    [2, "Henry", 80000, 4],
    [3, "Sam", 60000, None],
    [4, "Max", 90000, None],
]
Employee = pd.DataFrame(data, columns=["id", "name", "salary", "managerId"]).astype(
    {"id": "Int64", "name": "object", "salary": "Int64", "managerId": "Int64"}
)

# Finding employees who earn more than their managers
result = Employee[
    Employee.salary > Employee.set_index("id").loc[Employee.managerId, "salary"].values
].name
print(result)
