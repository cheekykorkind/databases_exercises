class SensorDataController < ApplicationController
  before_action :set_project
  before_action :set_sensor_datum, only: [:show, :update, :destroy]
  rescue_from ActiveRecord::RecordNotFound, with: :record_not_found

  # GET /sensor_data or /sensor_data.json
  def index
    render json: @project.sensors.sensor_datums, only: [:id, :data]
  end

  # GET /sensor_data/1 or /sensor_data/1.json
  def show
    render json: @sensor_datum, only: [:id, :data]
  end

  # POST /sensor_data or /sensor_data.json
  def create
    @sensor_datum = @project.sensors.sensor_datums.build(sensor_params)

    if @sensor_datum.save
      render json: @sensor_datum, status: :created, location: @sensor_datum
    else
      render json: @sensor_datum.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /sensor_data/1 or /sensor_data/1.json
  def update
    if @sensor_datum.update(sensor_datum_params)
      render json: @sensor_datum, status: :ok, only: [:id, :data]
    else
      render json: @sensor_datum.errors, status: :unprocessable_entity
    end
  end

  # DELETE /sensor_data/1 or /sensor_data/1.json
  def destroy
    @sensor_datum.destroy!
    head :no_content
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_project
      @project = Project.find(params[:project_id])
    end

    def set_sensor_datum
      @sensor_datum = @project.sensors.sensor_datums.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def sensor_datum_params
      params.expect(sensor_datum: [ :data ])
    end

    def record_not_found
      render json: { error: "Data not found" }, status: :not_found
    end
end
