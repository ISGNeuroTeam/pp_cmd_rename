from pp_exec_env.base_command import BaseCommand, Syntax, Rule, pd


class RenameCommand(BaseCommand):
    syntax = Syntax([Rule(name="col", type="arg", input_types=['string', 'term'], inf=True, )],  # must_be_a_field=True
                    use_timewindow=False)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        cols = self.get_arg('col')
        df.rename(
            {initial_name.value: initial_name.named_as for initial_name in cols},
            axis=1,
            inplace=True,
            errors='raise'
        )

        return df
