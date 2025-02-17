import spacy

def analyze_contracts(contract_text):
    """
    Analyze contracts for legal and compliance risks using NLP.
    """
    # Load SpaCy model
    nlp = spacy.load("en_core_web_sm")

    # Process contract text
    doc = nlp(contract_text)

    # Example: Extract key clauses
    key_clauses = [sent.text for sent in doc.sents if "indemnification" in sent.text.lower()]

    return key_clauses

def analyze_regulatory_filings(filing_text):
    """
    Analyze regulatory filings for compliance risks using NLP.
    """
    # Load SpaCy model
    nlp = spacy.load("en_core_web_sm")

    # Process filing text
    doc = nlp(filing_text)

    # Example: Extract risk-related sentences
    risk_sentences = [sent.text for sent in doc.sents if "risk" in sent.text.lower()]

    return risk_sentences