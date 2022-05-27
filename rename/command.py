import pandas as pd
from otlang.sdk.syntax import Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax


class RenameCommand(BaseCommand):
    syntax = Syntax([Positional("col", otl_type=OTLType.TEXT, inf=True)])

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        cols = self.get_iter('col')
        df.rename(
            {initial_name.value: initial_name.named_as for initial_name in cols},
            axis=1,
            inplace=True,
            errors='raise'
        )

        return df
