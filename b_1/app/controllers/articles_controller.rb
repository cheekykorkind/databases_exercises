class ArticlesController < ApplicationController
  before_action :set_project
  before_action :set_article, only: %i[ show edit update destroy ]

  # GET /articles or /articles.json
  def index
    @articles = @project.articles
  end

  # GET /articles/1 or /articles/1.json
  def show
  end

  # GET /articles/new
  def new
    @article = @project.articles.build
  end

  # GET /articles/1/edit
  def edit
  end

  # POST /articles or /articles.json
  def create
    @article = @project.articles.build(article_params)

    respond_to do |format|
      if @article.save
        format.html { redirect_to project_path(@project), notice: "Article was successfully created." }
      else
        format.html { render :new, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /articles/1 or /articles/1.json
  def update
    respond_to do |format|
      if @article.update(article_params)
        format.html { redirect_to project_path(@project), notice: "Article was successfully updated.", status: :see_other }
      else
        format.html { render :edit, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /articles/1 or /articles/1.json
  def destroy
    @article.destroy!

    respond_to do |format|
      format.html { redirect_to project_path(@project), notice: "Article was successfully destroyed.", status: :see_other }
    end
  end

  private
    def set_project
      @project = Project.find(params[:project_id])
    end

    def set_article
      @article = @project.articles.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def article_params
      params.require(:article).permit(:content)
    end
end
