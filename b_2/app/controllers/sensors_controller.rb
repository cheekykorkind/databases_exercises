class SensorsController < ApplicationController
  before_action :set_sensor, only: %i[ show edit update destroy ]
  rescue_from ActiveRecord::RecordNotFound, with: :record_not_found

  # GET /sensors or /sensors.json
  def index
    @sensors = Sensor.all
    render json: @sensors, only: [:id, :name]
  end

  # GET /sensors/1 or /sensors/1.json
  def show
    render json: @sensor, only: [:id, :name]
  end

  # GET /sensors/new
  def new
    @sensor = Sensor.new
  end

  # GET /sensors/1/edit
  def edit
  end

  # POST /sensors or /sensors.json
  def create
    @sensor = Sensor.new(sensor_params)

    if @sensor.save
      render json: @sensor, status: :created, location: @sensor
    else
      render json: @sensor.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /sensors/1 or /sensors/1.json
  def update
    if @sensor.update(sensor_params)
      render json: @sensor, status: :ok, only: [:id, :name, :memo]
    else
      render json: @sensor.errors, status: :unprocessable_entity
    end
  end

  # DELETE /sensors/1 or /sensors/1.json
  def destroy
    @sensor.destroy!
    head :no_content
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_sensor
      @sensor = Sensor.find(params.expect(:id))
    end

    # Only allow a list of trusted parameters through.
    def sensor_params
      params.expect(sensor: [ :project_id, :name ])
    end


    def record_not_found
      render json: { error: "Data not found" }, status: :not_found
    end
end
