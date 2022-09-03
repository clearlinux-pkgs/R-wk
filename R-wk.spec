#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-wk
Version  : 0.6.0
Release  : 7
URL      : https://cran.r-project.org/src/contrib/wk_0.6.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/wk_0.6.0.tar.gz
Summary  : Lightweight Well-Known Geometry Parsing
Group    : Development/Tools
License  : MIT
Requires: R-wk-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
well-known binary and well-known text representation of
  geometries to and from R-native formats. 
  Well-known binary is compact
  and fast to parse; well-known text is human-readable
  and is useful for writing tests. These formats are only
  useful in R if the information they contain can be 
  accessed in R, for which high-performance functions 
  are provided here.

%package lib
Summary: lib components for the R-wk package.
Group: Libraries

%description lib
lib components for the R-wk package.


%prep
%setup -q -c -n wk
cd %{_builddir}/wk

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641239080

%install
export SOURCE_DATE_EPOCH=1641239080
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library wk
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library wk
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library wk
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc wk || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/wk/DESCRIPTION
/usr/lib64/R/library/wk/INDEX
/usr/lib64/R/library/wk/LICENSE
/usr/lib64/R/library/wk/Meta/Rd.rds
/usr/lib64/R/library/wk/Meta/features.rds
/usr/lib64/R/library/wk/Meta/hsearch.rds
/usr/lib64/R/library/wk/Meta/links.rds
/usr/lib64/R/library/wk/Meta/nsInfo.rds
/usr/lib64/R/library/wk/Meta/package.rds
/usr/lib64/R/library/wk/NAMESPACE
/usr/lib64/R/library/wk/NEWS.md
/usr/lib64/R/library/wk/R/wk
/usr/lib64/R/library/wk/R/wk.rdb
/usr/lib64/R/library/wk/R/wk.rdx
/usr/lib64/R/library/wk/help/AnIndex
/usr/lib64/R/library/wk/help/aliases.rds
/usr/lib64/R/library/wk/help/paths.rds
/usr/lib64/R/library/wk/help/wk.rdb
/usr/lib64/R/library/wk/help/wk.rdx
/usr/lib64/R/library/wk/html/00Index.html
/usr/lib64/R/library/wk/html/R.css
/usr/lib64/R/library/wk/include/wk-v1-impl.c
/usr/lib64/R/library/wk/include/wk-v1.h
/usr/lib64/R/library/wk/include/wk/coord.hpp
/usr/lib64/R/library/wk/include/wk/error-formatter.hpp
/usr/lib64/R/library/wk/include/wk/experimental/wk-v1-filter-cpp11.hpp
/usr/lib64/R/library/wk/include/wk/experimental/wk-v1-handler-cpp11.hpp
/usr/lib64/R/library/wk/include/wk/experimental/wk-v1-reader-cpp11.hpp
/usr/lib64/R/library/wk/include/wk/fields.hpp
/usr/lib64/R/library/wk/include/wk/filter.hpp
/usr/lib64/R/library/wk/include/wk/geometry-debug-handler.hpp
/usr/lib64/R/library/wk/include/wk/geometry-formatter.hpp
/usr/lib64/R/library/wk/include/wk/geometry-handler.hpp
/usr/lib64/R/library/wk/include/wk/geometry-meta.hpp
/usr/lib64/R/library/wk/include/wk/geometry.hpp
/usr/lib64/R/library/wk/include/wk/io-bytes.hpp
/usr/lib64/R/library/wk/include/wk/io-string.hpp
/usr/lib64/R/library/wk/include/wk/io.hpp
/usr/lib64/R/library/wk/include/wk/parse-exception.hpp
/usr/lib64/R/library/wk/include/wk/rcpp-coord-reader.hpp
/usr/lib64/R/library/wk/include/wk/rcpp-io.hpp
/usr/lib64/R/library/wk/include/wk/rcpp-translate.hpp
/usr/lib64/R/library/wk/include/wk/rct.hpp
/usr/lib64/R/library/wk/include/wk/reader.hpp
/usr/lib64/R/library/wk/include/wk/wkb-reader.hpp
/usr/lib64/R/library/wk/include/wk/wkb-writer.hpp
/usr/lib64/R/library/wk/include/wk/wkt-reader.hpp
/usr/lib64/R/library/wk/include/wk/wkt-streamer.hpp
/usr/lib64/R/library/wk/include/wk/wkt-writer.hpp
/usr/lib64/R/library/wk/include/wk/writer.hpp
/usr/lib64/R/library/wk/include/wk/xyzm.hpp
/usr/lib64/R/library/wk/tests/testthat.R
/usr/lib64/R/library/wk/tests/testthat/Rplots.pdf
/usr/lib64/R/library/wk/tests/testthat/test-affine.R
/usr/lib64/R/library/wk/tests/testthat/test-bbox.R
/usr/lib64/R/library/wk/tests/testthat/test-chunk.R
/usr/lib64/R/library/wk/tests/testthat/test-class-data-frame.R
/usr/lib64/R/library/wk/tests/testthat/test-count.R
/usr/lib64/R/library/wk/tests/testthat/test-crc.R
/usr/lib64/R/library/wk/tests/testthat/test-debug.R
/usr/lib64/R/library/wk/tests/testthat/test-filter.R
/usr/lib64/R/library/wk/tests/testthat/test-flatten.R
/usr/lib64/R/library/wk/tests/testthat/test-format.R
/usr/lib64/R/library/wk/tests/testthat/test-handle-crc.R
/usr/lib64/R/library/wk/tests/testthat/test-handle-rct.R
/usr/lib64/R/library/wk/tests/testthat/test-handle-sfc.R
/usr/lib64/R/library/wk/tests/testthat/test-handle-slice.R
/usr/lib64/R/library/wk/tests/testthat/test-handle-wkb.R
/usr/lib64/R/library/wk/tests/testthat/test-handle-wkt.R
/usr/lib64/R/library/wk/tests/testthat/test-handle-xy.R
/usr/lib64/R/library/wk/tests/testthat/test-handler.R
/usr/lib64/R/library/wk/tests/testthat/test-make.R
/usr/lib64/R/library/wk/tests/testthat/test-meta.R
/usr/lib64/R/library/wk/tests/testthat/test-pkg-readr.R
/usr/lib64/R/library/wk/tests/testthat/test-pkg-sf.R
/usr/lib64/R/library/wk/tests/testthat/test-pkg-vctrs.R
/usr/lib64/R/library/wk/tests/testthat/test-plot.R
/usr/lib64/R/library/wk/tests/testthat/test-problems.R
/usr/lib64/R/library/wk/tests/testthat/test-rct.R
/usr/lib64/R/library/wk/tests/testthat/test-set.R
/usr/lib64/R/library/wk/tests/testthat/test-sfc-writer.R
/usr/lib64/R/library/wk/tests/testthat/test-transform.R
/usr/lib64/R/library/wk/tests/testthat/test-translate.R
/usr/lib64/R/library/wk/tests/testthat/test-utils.R
/usr/lib64/R/library/wk/tests/testthat/test-vertex-filter.R
/usr/lib64/R/library/wk/tests/testthat/test-void.R
/usr/lib64/R/library/wk/tests/testthat/test-wk-crs.R
/usr/lib64/R/library/wk/tests/testthat/test-wk-rcrd.R
/usr/lib64/R/library/wk/tests/testthat/test-wk-vctr.R
/usr/lib64/R/library/wk/tests/testthat/test-wkb-writer.R
/usr/lib64/R/library/wk/tests/testthat/test-wkb.R
/usr/lib64/R/library/wk/tests/testthat/test-wkt-writer.R
/usr/lib64/R/library/wk/tests/testthat/test-wkt.R
/usr/lib64/R/library/wk/tests/testthat/test-writer.R
/usr/lib64/R/library/wk/tests/testthat/test-xy-writer.R
/usr/lib64/R/library/wk/tests/testthat/test-xyzm.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/wk/libs/wk.so
/usr/lib64/R/library/wk/libs/wk.so.avx2
/usr/lib64/R/library/wk/libs/wk.so.avx512
