# import pandas as pd
#
# df = pd.read_csv('data.csv')
#
# print(df.to_string())

# import pandas as pd
#
# print(pd.options.display.max_rows)

import pandas as pd

d = pd.date_range('11-Sep-2017', '17-Sep-2017', freq='2D')


len(d[d.isin(pd.to_datetime(['12-09-2017', '15-09-2017']))])