template<class Chave, class Item>
void ABB<Chave,Item>::show (No<Chave,Item>* root) {
	
	if (root == nullptr)
		return;

	this->show (root->esq);

	cout << "Nº: " << this->rank(root->getChave()) << "\tPalavra: " << root->getChave() << "\tOcorrencias: " << root->getValor() << endl;

	this->show (root->dir);

}

