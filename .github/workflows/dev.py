# name: Deploy to dev

# concurrency:
#   group: deploy-dev
#   cancel-in-progress: true

# on:
#   workflow_dispatch:

#   pull_request:
#     types:
#       - opened
#       - synchronize
#     branches:
#       - main
#     paths:
#       - "**/*.yml"
#       - "**/*.py"

# jobs:
#   deploy:
#     name: "Deploy bundle"
#     runs-on: ubuntu-latest

#     steps:
#       - uses: actions/checkout@v3

#       - uses: databricks/setup-cli@main

#       - run: databricks bundle deploy
#         env:
#           DATABRICKS_TOKEN: ${{ secrets.DATABRICKS_TOKEN }}
#           DATABRICKS_BUNDLE_ENV: dev

#   pipeline_update:
#     name: "Run pipeline update"
#     runs-on: ubuntu-latest

#     needs:
#       - deploy

#     steps:
#       - uses: actions/checkout@v3 

#       - uses: databricks/setup-cli@main

#       - shell: bash
#         name: Run pipeline update
#         run: |
#           set -o pipefail
#           databricks bundle run test_dabs_job --refresh-all 2>&1 | tee output.log

#         # - run: databricks bundle run fe_medium_metrics --refresh-all
#         env:
#           DATABRICKS_TOKEN: $ {{ secrets.DATABRICKS_TOKEN }}
#           DATABRICKS_BUNDLE_ENV: dev
