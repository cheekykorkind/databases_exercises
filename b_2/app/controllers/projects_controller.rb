class ProjectsController < ApplicationController
  before_action :set_project, only: %i[ show edit update destroy ]
  rescue_from ActiveRecord::RecordNotFound, with: :record_not_found


  # GET /projects or /projects.json
  def index
    @projects = Project.all
    render json: @projects, only: [:id, :name, :memo]
  end

  # GET /projects/1 or /projects/1.json
  def show
    render json: @project, only: [:id, :name, :memo]
  end

  # GET /projects/new
  def new
    @project = Project.new
  end

  # GET /projects/1/edit
  def edit
  end

  # POST /projects or /projects.json
  def create
    @project = Project.new(project_params)

    if @project.save
      render json: @project, status: :created, location: @project
    else
      render json: @project.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /projects/1 or /projects/1.json
  def update
    if @project.update(project_params)
      render json: @project, status: :ok, only: [:id, :name, :memo]
    else
      render json: @project.errors, status: :unprocessable_entity
    end
  end

  # DELETE /projects/1 or /projects/1.json
  def destroy
    @project.destroy!
    head :no_content
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_project
      @project = Project.find(params.expect(:id))
    end

    # Only allow a list of trusted parameters through.
    def project_params
      params.expect(project: [ :name, :memo ])
    end

    def record_not_found
      render json: { error: "Data not found" }, status: :not_found
    end
end
