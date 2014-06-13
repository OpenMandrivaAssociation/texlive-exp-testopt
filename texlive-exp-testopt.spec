# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/exp-testopt
# catalog-date 2009-03-08 17:38:29 +0100
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-exp-testopt
Version:	0.3
Release:	7
Summary:	Expandable \@testopt (and related) macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exp-testopt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exp-testopt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exp-testopt.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exp-testopt.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an expandable variant of the LaTeX kernel
command \@testopt, named \@expandable@testopt, and a more
general \@expandable@ifopt, both intended for package writers.
Also we have a variant of \newcommand which uses these macros
to check for optional arguments.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/exp-testopt/exp-testopt.sty
%doc %{_texmfdistdir}/doc/latex/exp-testopt/README
%doc %{_texmfdistdir}/doc/latex/exp-testopt/exp-testopt.pdf
%doc %{_texmfdistdir}/doc/latex/exp-testopt/exp-testopt.test
#- source
%doc %{_texmfdistdir}/source/latex/exp-testopt/exp-testopt.dtx
%doc %{_texmfdistdir}/source/latex/exp-testopt/exp-testopt.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-2
+ Revision: 751727
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 718402
- texlive-exp-testopt
- texlive-exp-testopt
- texlive-exp-testopt
- texlive-exp-testopt

