def set_continue_downstream(value: str = "no"):
    """
    Sets the 'continue_downstream' task value for the current Databricks job run.

    Parameters:
        value (str): The value to set ('yes' or 'no'). Defaults to 'no'.
    """
    dbutils.jobs.taskValues.set(key="continue_downstream", value=value)