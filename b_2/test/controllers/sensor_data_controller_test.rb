require "test_helper"

class SensorDataControllerTest < ActionDispatch::IntegrationTest
  setup do
    @sensor_datum = sensor_data(:one)
  end

  test "should get index" do
    get sensor_data_url
    assert_response :success
  end

  test "should get new" do
    get new_sensor_datum_url
    assert_response :success
  end

  test "should create sensor_datum" do
    assert_difference("SensorDatum.count") do
      post sensor_data_url, params: { sensor_datum: { data: @sensor_datum.data, sensor_id: @sensor_datum.sensor_id } }
    end

    assert_redirected_to sensor_datum_url(SensorDatum.last)
  end

  test "should show sensor_datum" do
    get sensor_datum_url(@sensor_datum)
    assert_response :success
  end

  test "should get edit" do
    get edit_sensor_datum_url(@sensor_datum)
    assert_response :success
  end

  test "should update sensor_datum" do
    patch sensor_datum_url(@sensor_datum), params: { sensor_datum: { data: @sensor_datum.data, sensor_id: @sensor_datum.sensor_id } }
    assert_redirected_to sensor_datum_url(@sensor_datum)
  end

  test "should destroy sensor_datum" do
    assert_difference("SensorDatum.count", -1) do
      delete sensor_datum_url(@sensor_datum)
    end

    assert_redirected_to sensor_data_url
  end
end
