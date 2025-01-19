# TODO list

- add docs website
- add more proper examples
- add http status categories - ie 'is_informational', is successfull' etc.
- suggest retry logic (`should_retry()`) returning a bool if code is retryable
  (ie `408`, `429`, `500`, `503`, `504`)
- API friendly output - ie returning:

    ```python
    return {
        "status": "error",
        "code": cls.error_code,
        "message": cls.message
    }
    ```

- json serialization ie returning:

    ```json
    {"error_code": 404, "message": "Not Found"}
    ```

- integration with logging libraries
