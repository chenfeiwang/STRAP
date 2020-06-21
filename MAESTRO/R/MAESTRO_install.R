# install required R packages
library(devtools)

BiocManager::install("org.Hs.eg.db")
BiocManager::install("org.Mm.eg.db")
install_github("chenfeiwang/MAESTRO", upgrade = "never")
install_github("hms-dbmi/pagoda2", upgrade = "never")
install_github("SUwonglab/scABC@v0.1", upgrade = "never")
install_github("GreenleafLab/chromVARmotifs", upgrade = "never")
# install_version(package = "Seurat", version = "3.0.2", repos="https://mirrors.tongji.edu.cn/CRAN/")

