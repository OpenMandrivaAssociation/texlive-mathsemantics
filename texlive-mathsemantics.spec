Name:		texlive-mathsemantics
Version:	63241
Release:	2
Summary:	Semantic math commands in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathsemantics
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathsemantics.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathsemantics.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides both syntactic and semantic helpers
to typeset mathematics in LaTeX. The syntactic layer eases
typesetting of formulae in general, while the semantic layer
provides commands like \inner{x}{y} to unify typesetting of
inner products. These not only unify typesetting of math
formulae but also allow to easily adapt notation if a user
prefers to. The semantic layer is split into topics.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/mathsemantics
%doc %{_texmfdistdir}/doc/latex/mathsemantics

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
