%global packname  modeltools
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.2_19
Release:          1
Summary:          Tools and Classes for Statistical Models
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-19.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-stats R-stats4 
Requires:         R-methods 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-stats4
BuildRequires:    R-methods 

%description
A collection of tools to deal with statistical models. The functionality
is experimental and the user interface is likely to change in the future.
The documentation is rather terse, but packages `coin' and `party' have
some working examples. However, if you find the implemented ideas
interesting we would be very interested in a discussion of this proposal.
Contributions are more than welcome!

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
