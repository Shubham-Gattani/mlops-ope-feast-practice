**Commands executed**

1. **Create BigQuery dataset**
   Run from anywhere:

   ```
   bq --project_id=mlops-iris-week1-graded --location=US mk -d feast_iris
   ```

2. **Load CSV into BigQuery**
   Run from repo root:

   ```
   bq load --project_id=mlops-iris-week1-graded --location=US \
   --source_format=CSV --autodetect feast_iris.iris_features \
   ./iris_data_adapted_for_feast.csv
   ```

3. **Create Feast repo structure**
   Run inside `feast_artifacts/`:

   ```
   feast init iris_repo
   ```

4. **Apply Feast repo**
   Run inside:

   ```
   feast_artifacts/iris_repo/feature_repo
   ```

   Command:

   ```
   feast apply
   ```

5. **Materialize data to SQLite online store**
   Run inside same folder:

   ```
   feast materialize-incremental "$(date +%Y-%m-%d)"
   ```

6. **Test online retrieval**
   Python, executed inside:

   ```
   feast_artifacts/iris_repo/feature_repo
   ```

**Files created (no code, just locations)**

1. `feast_artifacts/iris_repo/feature_repo/feature_store.yaml`
   (overwritten with BigQuery + SQLite config)

2. `feast_artifacts/iris_repo/feature_repo/iris_features.py`
   (FeatureView + Entity + BigQuerySource)

3. `feast_artifacts/iris_repo/registry.db`
   (created by `feast apply`)

4. `feast_artifacts/iris_repo/online_store.db`
   (created + filled during materialization)

This is the minimal end-to-end pipeline summary.
