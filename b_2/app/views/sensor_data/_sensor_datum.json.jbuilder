json.extract! sensor_datum, :id, :sensor_id, :data, :created_at, :updated_at
json.url sensor_datum_url(sensor_datum, format: :json)
