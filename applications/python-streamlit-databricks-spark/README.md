# Streamlit with Databricks Example

This is a simple example of a Streamlit app that runs on Workbench and Connect.

> **Warning**
> The version of `databricks-connect` that you install depends on your Databricks runtime https://docs.databricks.com/aws/en/release-notes/dbconnect/. In my case, I need to use `databricks-connect==14.3.7` because I have Databricks runtime `x`. This can also impact the versio of Python you use. For example `databricks-connect==14.3.7` does not support Python 3.12 in my testing (due to removal of `disutils` package), so I need to be explicity to use a version of Python less than 3.12.
