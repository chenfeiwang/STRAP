# install required R packages
library(devtools)

Sys.setenv(R_REMOTES_NO_ERRORS_FROM_WARNINGS="true")
BiocManager::install("org.Hs.eg.db", update=FALSE)
BiocManager::install("org.Mm.eg.db",  update=FALSE)
install_github("chenfeiwang/MAESTRO", upgrade = "never")
install_github("hms-dbmi/pagoda2", upgrade = "never")
install_github("SUwonglab/scABC@v0.1", upgrade = "never")
install_github("GreenleafLab/chromVARmotifs", upgrade = "never")
# install_version(package = "Seurat", version = "3.0.2", repos="https://mirrors.tongji.edu.cn/CRAN/")

