from pandas.io.clipboards import read_clipboard as read_clipboard
from pandas.io.excel import (
    ExcelFile as ExcelFile,
    ExcelWriter as ExcelWriter,
    read_excel as read_excel,
)
from pandas.io.feather_format import read_feather as read_feather
from pandas.io.gbq import read_gbq as read_gbq
from pandas.io.html import read_html as read_html
from pandas.io.json import read_json as read_json
from pandas.io.orc import read_orc as read_orc
from pandas.io.parquet import read_parquet as read_parquet
from pandas.io.parsers import (
    read_csv as read_csv,
    read_fwf as read_fwf,
    read_table as read_table,
)
from pandas.io.pickle import (
    read_pickle as read_pickle,
    to_pickle as to_pickle,
)
from pandas.io.pytables import (
    HDFStore as HDFStore,
    read_hdf as read_hdf,
)
from pandas.io.sas import read_sas as read_sas
from pandas.io.spss import read_spss as read_spss
from pandas.io.sql import (
    read_sql as read_sql,
    read_sql_query as read_sql_query,
    read_sql_table as read_sql_table,
)
from pandas.io.stata import read_stata as read_stata
from pandas.io.xml import read_xml as read_xml
