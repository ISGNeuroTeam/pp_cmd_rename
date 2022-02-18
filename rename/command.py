from pp_exec_env.base_command import BaseCommand, Syntax, Rule, pd


class RenameCommand(BaseCommand):
    syntax = Syntax([Rule(name="col", type="arg", input_types=['string', 'term'], inf=True)],
                    use_timewindow=False)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        cols = self.get_arg('col')
        df.rename(
            {initial_name: initial_name.named_as for initial_name in cols}
        )

        return df
