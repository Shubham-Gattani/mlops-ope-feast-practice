from feast import Entity, FeatureView, Field, BigQuerySource
from feast.types import Float32, String
# from feast.data_source import BigQuerySource

iris_source = BigQuerySource(
    table="mlops-iris-week1-graded.feast_iris.iris_features",
    timestamp_field="event_timestamp",
    # created_timestamp_column="created_timestamp", # REMOVED FROM FEAST 0.31+
)

iris_entity = Entity(
    name="iris_id",
    join_keys=["iris_id"],
    description="Iris identifier",
)

iris_feature_view = FeatureView(
    name="iris_features_view",
    entities=[iris_entity],
    ttl=None,
    schema=[
        Field(name="sepal_length", dtype=Float32),
        Field(name="sepal_width", dtype=Float32),
        Field(name="petal_length", dtype=Float32),
        Field(name="petal_width", dtype=Float32),
        Field(name="species", dtype=String),
    ],
    online=True,
    source=iris_source,
)
